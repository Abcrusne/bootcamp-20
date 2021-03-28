
console.log("My JS is connected")
document.getElementById("send").innerHTML = "send";


$(document).ready(function(){
    console.log("this is my jquery")
    $("#send").on('click', function(){
       socket.send($("#msg").val())
    })
// socket.on('connect', function() {
        
    if(!localStorage.username){
        $('#myModal').modal({backdrop: 'static', keyboard: false});
        $('.modal-title').text("Type in your username");
        $('#modalInput').val("");
    }

    socket.on("msgs", data => {
        console.log("this is data from get msgs " + data);
        $('#display-message-area').text("");
        // forEach = tos msg visa data
        data.forEach(msg => {
            console.log(msg)
            show_msg(msg)
        })
    })

    socket.on('add username', data =>{
        localStorage.setItem('username', data["username"]);
        $('#username').text(localStorage.username)
    })

    socket.on('message', data =>{
        const p = document.createElement('p');
        p.innerHTML = data.msg;
        const span = document.createElement('span');
        span.innerHTML = data.username;
        if (data.username == localStorage.username)
        console.log("message was sent")
        $(span).addClass("user-style")
        const time = document.createElement('p');
        // to butent stringo laika ir data
        time.innerHTML = new Date().toLocaleString();
        $('#display-message-area').append(p);
        $('#display-message-area').append(span);
        $('#display-message-area').append(time);
        $('#display-message-area').scrollTop(5000)
    });

    $('#modalInput').on('keyup', function(key) {
        if($(this).val().length > 0){
            $('#modalButton').attr('disabled', false)
            if(key.keyCode == 13){
                $('#modalButton').click()
            }
        }
        else{
            $('#modalButton').attr('disabled', true)
        }
    });

    $('#modalButton').on('click', function(){
        //action for new username
        if(!localStorage.getItem('username')){
            var username = $('#modalInput').val();
            socket.emit('new username', {'username': username})
        }
    })

    $('#message').on('keyup', function(key){
        if(key.keyCode == 13){//Enter key pressed
            $('#send-message').click();//Trigger search button click event
        }
    });

    $('#send-message').on('click', function(){
        time = new Date().toLocaleString();
        socket.send({'msg': $('#message').val(), 'username': localStorage.username, 'time': time}, )
        $('#message').val("");
    })

    function printMsg(msg) {
        const p = document.createElement('p')
        p.innerHTML = msg;
        $('#display-message-area').append(p);
    }
    const show_msg = data => {

        let div = $("#display-message-area");
        let p = document.createElement("p");
        let span = document.createElement("span")
        let time = document.createElement("span")
    
      //   p.classList.add("list-group-item");
        p.innerHTML = data.msg
        span.innerHTML = data.username
        time.innerHTML = data.time
    
  
        div.append(p);
        div.append(span)
        div.append(time)
      
    };




});



//     socket.on('message', data =>{
//         const p = document.createElement('p');
//         p.innerHTML = data;
//         $('#display-msg').append(p);
//     })
//     socket.on('add username', data =>{
//         localStorage.setItem('username', data["username"]);
//         $('#username').text(localStorage.username)
//     })
//   });