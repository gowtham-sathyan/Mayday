$(document).ready(function() {
    $('select').material_select();
});
$('#registerBtn').click(function(){
    var fname=$('#first_name').val();
    var lname=$('#last_name').val();
    var email=$('#email').val();
    var pwd=$('#password').val();
    var mobile=$('#mobile').val();
    var state=$('#state').val();
    var city=$('#city').val().toLowerCase();
    if(!fname||!lname||!email||!pwd||!mobile||!state||!city){alert('Please make sure that all the inputs are filled');}
    else {
        console.log(fname, lname, email, pwd, mobile, state, city);
        var data=JSON.stringify({fname:fname,lname:lname,email:email,pwd:pwd,mobile:mobile,state:state,city:city});
        console.log(data);
        var obj=new XMLHttpRequest();
        obj.open('POST','http://localhost:8000/registration',true);
        obj.setRequestHeader('Content-Type','application/json');
        obj.send(data);
        }

});




