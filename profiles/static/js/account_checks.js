$(document).ready(function(){
        $("#form1").validate({
	   rules: {
                    username: {
                        required: true,
                        minlength: 3,
                        usercheck: true
                    },
                    first_name: {
                        required: true
                    },
                    email: {
                        required: true,
                        emailcheck: true,
                    },
            },
            messages: {
                    username: {
                        required: "Enter username",
                        minlength: "Enter atleast 3 characters",
                        usercheck: "Enter alphanumeric and underscore only",
                    },
                    first_name: {
                        required: "Enter firstname"
                    },
                    email: {
                        required: "Enter email",
                        emailcheck: "Enter valid email"
                    },
            },
            errorPlacement: function ($error, $element) {
                    var name = $element.attr("name");                 
                    $("#error" + name).append($error);
            },
        });
        
        $.validator.addMethod("usercheck",
            function(value, element) {
            return /^[A-Za-z0-9_]+$/.test(value);
            });
            
        $.validator.addMethod("emailcheck",
            function(value, element) {
            return /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,4}$/.test(value);
            });
    });
