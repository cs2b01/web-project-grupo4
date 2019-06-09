function getData() {
    $('#action').html('Autenticando...');
    var email = $('#email').val();
    var password = $('#password').val();
    var message = JSON.stringify({
            "email": email,
            "password": password
        });

    $.ajax({
        url: '/authenticate',
        type: 'POST',
        contentType: 'application/json',
        data: message,
        dataType: 'json',
        success: function (response) {

        },
        error: function (response) {
            if (response['status'] == 401) {
                //document.getElementById("barra_login").style.display = "none";
                $('#action').html('<a>Sesión iniciada</a>')
            } else {
                //document.getElementById("barra_login").style.display = "none";
                $('#action').html('<a>Usuario y/o contraseña incorrectos</a>');
                //document.getElementById("barra_login").style.display = "inline";
            }
        }
    });
}