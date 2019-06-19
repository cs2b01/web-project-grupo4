function cargar_datos() {
    get_restaurant();
    get_menu();
}

    function get_menu() {
        $.ajax({
            url:'/menu',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                $.each(response,function (index,value) {
                    if (response[index]['tipo_plato'] === "segundo"){
                        $('#segundos').append('<li>'+value.name+'</li>');
                    } else if (response[index]['tipo_plato'] === "entrada"){
                        $('#entradas').append('<li>'+value.name+'</li>');
                    }
                })
            },
            error: function(error){
                alert(JSON.stringify(error));
            }
        });
    }

    function get_restaurant() {
        $.ajax({
            url:'/restaurant',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                //alert(response["name_restaurant"]);
                $('h1').text(response["name_restaurant"]);
                $('#slogan').text(response["slogan"]);
                $('#phone').html(' Teléfono <a href="tel:+51'+response['phone']+'">+51 '+response['phone']+'</a>');
                $('#mail').html(' Email <a href="mailto:'+response['username']+'">'+response['username']+'</a>')
                $('#adress').html(' Dirección '+response['address']);
                $('#mesas').text(response['num_mesas'])
            },
            error: function(error){
                alert(error);
            }
        });
    }
