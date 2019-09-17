# gRPC Python Implementation

<b>gRPC (gRPC Remote Procedure Calls)</b> is an open source remote procedure call (RPC) system initially developed at Google. 
It uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, 
bidirectional streaming and flow control, blocking or nonblocking bindings, and cancellation and timeouts. 
It generates cross-platform client and server bindings for many languages. Most common usage scenarios include 
connecting services in microservices style architecture and connect mobile devices, browser clients to backend services.
![Alt Text](https://miro.medium.com/max/3138/1*TatrFsqJoxF9Vr3r4UVayQ.png)

<h2>Why gRPC?</h2>
gRPC is a modern open source high performance RPC framework that can run in any environment. 
It can efficiently connect services in and across data centers with pluggable support for load balancing, 
tracing, health checking and authentication. 
It is also applicable in last mile of distributed computing to connect devices, mobile applications and browsers to backend services.

* Simple service definition
     - Define your service using Protocol Buffers, a powerful binary serialization toolset and language
* Works across languages and platforms
     - Automatically generate idiomatic client and server stubs for your service in a variety of languages and platforms
* Start quickly and scale
     - Install runtime and dev environments with a single line and also scale to millions of RPCs per second with the framework
* Bi-directional streaming and integrated auth
     - Bi-directional streaming and fully integrated pluggable authentication with http/2 based transport
     
<h2>How GRPC Works?</h2>

* A client application is able to call methods directly on a server-side application present on other machines.
* Service is defined, methods are specified which can be further remotely called with their parameters and return types.
* On the other hand, the server runs a GRPC server to handle client calls.
* It uses protocol buffers as the Interface Definition Language to enable communication between two different systems used for describing the service interface and the structure of payload messages.
* HTTP/2 – GRPC is basically a protocol built on top of HTTP/2. HTTP/2 is used as a transport.
* Protobuf serialization – Messages that we serialize both for the request and response are encoded with protocol buffers.
* Clients open one long-lived connection to GRPC server.
* A new HTTP/2 stream for each RPC call.
* Allows Client-Side and Server-Side Streaming.
* Bidirectional Streaming.

<h2>Transfer Protocols</h2>

* Rest is heavily dependent on HTTP 1.1, and on the other hand, GRPC based on HTTP/2. HTTP 2 is Binary protocol, and HTTP 1.1 is Textual. Binary protocol is much efficient to parse and its safe.
* HTTP 2 is multiplexing in nature. It overcomes the Head-of-Line Blocking problem. In HTTP 1.1, where there is many request P Client, then each request are served one by one. Due to which slow request slows down all the other subsequent request. But HTTP 2 has the capability of serving the multiple request and response at the same time called MultiPlexing.
* HTTP 2 uses header compression to reduce overhead (resolved excess time and memory problem).
* HTTP 2 also enables Duplex Streaming, in other words, HTTP 2 allows reading and writing simultaneously, without requiring line turnarounds. Reading and writing events are independent of each other.

<h2>Streaming Vs Request/Response</h2>

* When talking about REST, it uses the request-response model but on the other hand, GRPC is taking the full advantages of HTTP 2 and allows us to stream the information constantly in various streaming options provided by HTTP 2.
* Server Streaming – In this type of streaming, Server delivers the content or information to the client either live or on demand.
* Client Streaming – In Client streaming, let’s say an example, a client writes a sequence of messages and after that send them to the server as a stream. And then the client will wait for the server to read them and return the response.
* Bidirectional Streaming – This type of streaming initiated by the client and further, there are two cases, either the server has to wait till all the client’s messages has been received on the client side or the server and client starts doing ping-pong to each other, means both server and client both able to communicate another hand independently in a full-duplex fashion.

<h2>Why not REST?</h2>

* While creating RESTful services, most of us follow a standard practice of writing client library and all we need to do is update client library whenever there is a change in api contracts.
* Streaming is difficult and its highly impossible in most of the languages.
* Duplex streaming is not possible.
* Hard to get multiple resources in single request.
* Need semantic versioning whenever the api contract needs to be changed.
