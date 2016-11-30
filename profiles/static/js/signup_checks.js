$(document).ready(function(){
        $("#form1").validate({
	   rules: {
                    account-username: {
                        required: true,
                        minlength: 3,
                        usercheck: true
                    },
                    account-first_name: {
                        required: true
                    },
                    account-password: {
                        required: true,
                        pwcheck: true
                    },
                    account-retype: {
                        equalTo: "#id_password"
                    },
                    account-email: {
                        required: true,
                        emailcheck: true,
                    },
            },
            messages: {
                    account-username: {
                        required: "Enter username",
                        minlength: "Enter atleast 3 characters",
                        usercheck: "Enter alphanumeric and underscore only",
                    },
                    account-first_name: {
                        required: "Enter firstname"
                    },
                    account-password: {
                        required: "Enter password",
                        pwcheck: "Must contain one capital letter, one small letter, one digit and length between 5-12 characters"
                    },
                    account-retype: {
                        equalTo: "Enter same password again"
                    },
                    account-email: {
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
        
        $.validator.addMethod("pwcheck",
            function(value, element) {
            return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{5,12}$/.test(value);
            });
            
        $.validator.addMethod("emailcheck",
            function(value, element) {
            return /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,4}$/.test(value);
            });
    });
