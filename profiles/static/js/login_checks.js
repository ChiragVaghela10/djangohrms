$(document).ready(function(){
        $("#form1").validate({
            rules: {
                    username: {
                        required: true,
                        minlength: 3,
                        usercheck: true
                    },
                    password: {
                        required: true,
                        pwcheck: true
                    },
            },
            messages: {
                    username: {
                        required: "Enter username",
                        minlength: "Enter atleast 3 characters",
                        usercheck: "Enter alphanumeric and underscore only",
                    },
                    password: {
                        required: "Enter password",
                        pwcheck: "Must contain one capital letter, one small letter, one digit and length between 5-12 characters"
                    },
            },
            errorPlacement: function ($error, $element) {
                    var name = $element.attr("name");                 
                    $("#error" + name).append($error);
            },
            });
            
        $.validator.addMethod("usercheck",
            function(value, element) {
            return /^[A-Za-z0-9_@.]+$/.test(value);
            });
        
        $.validator.addMethod("pwcheck",
            function(value, element) {
            return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{5,12}$/.test(value);
            });
    });
