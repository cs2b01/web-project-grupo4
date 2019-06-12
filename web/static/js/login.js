function getData() {
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
                alert('Datos incorrectos');
                print('Sesión no iniciada');
            } else {
                alert('Sesión iniciada');
                print('Sesión iniciada');
            }
        }
    });
}