write_socket = function() {

    var webSocket = new WebSocket("ws://127.0.0.1:1337");
    console.log("da");

    webSocket.onmessage = function(e) {
       console.log("Got echo: " + e.data);
    }
}