
var video = document.getElementById('video');
var canvas = document.getElementById('motion');
var score = document.getElementById('score');

function initSuccess() {
	DiffCamEngine.start();
}

function initError() {
	alert('Something went wrong.');
}

DiffCamEngine.init({
	video: video,
	motionCanvas: canvas,
	initSuccessCallback: initSuccess,
	initErrorCallback: initError,
	captureCallback: capture
});
  // Create a client instance
  client = new Paho.MQTT.Client("m15.cloudmqtt.com", 36819,"web_" + parseInt(Math.random() * 100, 10));
  //Example client = new Paho.MQTT.Client("m11.cloudmqtt.com", 32903, "web_" + parseInt(Math.random() * 100, 10));

  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  var options = {
    useSSL: true,
    userName: "vswyqwhc",
    password: "G4Mx5iGkb5Ol",
    onSuccess:onConnect,
    onFailure:doFail
  }

  // connect the client
  client.connect(options);

  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("onConnect");
    client.subscribe("/bettersense");
    message = new Paho.MQTT.Message("Hello CloudMQTT");
    message.destinationName = "/bettersense";
    client.send(message);
  }

  function doFail(e){
    console.log(e);
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }

  // called when a message arrives
  function onMessageArrived(message) {
    console.log("onMessageArrived:"+message.payloadString);
  }

  function capture(payload) {
    if (payload.score > 400){
      score.textContent = payload.score;
      message = new Paho.MQTT.Message("1");
      message.destinationName = "/bettersense";
      client.send(message);
    }
  }

  function send_red(){
    message = new Paho.MQTT.Message("red");
    message.destinationName = "/bettersense";
    client.send(message);
  }
  function send_yellow(){
    message = new Paho.MQTT.Message("yellow");
    message.destinationName = "/bettersense";
    client.send(message);
  }
  function send_green(){
    message = new Paho.MQTT.Message("green");
    message.destinationName = "/bettersense";
    client.send(message);
  }
  function send_aqua(){
    message = new Paho.MQTT.Message("aqua");
    message.destinationName = "/bettersense";
    client.send(message);
  }

  function send_orange(){
    message = new Paho.MQTT.Message("orange");
    message.destinationName = "/bettersense";
    client.send(message);
  }

  function send_blue(){
    message = new Paho.MQTT.Message("blue");
    message.destinationName = "/bettersense";
    client.send(message);
  }


  function send_white(){
    message = new Paho.MQTT.Message("white");
    message.destinationName = "/bettersense";
    client.send(message);
  }





