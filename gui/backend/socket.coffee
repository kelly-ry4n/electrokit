# send keys to websocket and echo the response
$(document).ready ->
  
  # create websocket
  # WebSocket = MozWebSocket  unless "WebSocket" of window # firefox
  socket = new WebSocket("ws://localhost:8076")
  
  # open the socket
  socket.onopen = (event) ->
    socket.send "connected\n"
    
    # show server response
    socket.onmessage = (e) ->
      # console.log e.data
      json_ar = e.data.split("\n")
      for json in json_ar
        # Play sound here
        console.log json
      # $("#output").text e.data
      return

    
    # for each typed key send #entry's text to server
    $("#entry").keyup (e) ->
      socket.send $("#entry").attr("value") + "\n"
      return

    return

  return
