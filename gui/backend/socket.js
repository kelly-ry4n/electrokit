// Generated by CoffeeScript 1.6.3
$(document).ready(function() {
  var socket;
  socket = new WebSocket("ws://localhost:8076");
  socket.onopen = function(event) {
    socket.send("connected\n");
    socket.onmessage = function(e) {
      var json, json_ar, _i, _len;
      json_ar = e.data.split("\n");
      print(json_ar);
      for (_i = 0, _len = json_ar.length; _i < _len; _i++) {
        json = json_ar[_i];
        console.log(json);
      }
    };
    $("#entry").keyup(function(e) {
      socket.send($("#entry").attr("value") + "\n");
    });
  };
});
