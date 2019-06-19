$(document).ready(function() {
    var i = 1;
    console.log("go");
    $("#add_entrada").click(function(){
        console.log("Agregar entrada");
        i++;
        input_fila = jQuery('<tr id="row'+i+'"><td><input type="text" name="entrada'+i+'" placeholder="Ingresar entrada" class="form-control entrada_list"></td><td><button name="del_entrada" id="'+i+'" class="btn btn-danger btn_remove">X</button></td></tr>');
        $("#tableform").append(input_fila);
        event.preventDefault();
    });
    var j = 1;
    $("#add_segundo").click(function(){
        console.log("Agregar segundo");
        j++;
        input_fila = jQuery('<tr id="rowseg'+j+'"><td><input type="text" name="segundo'+j+'" placeholder="Ingresar segundo" class="form-control segundo_list"></td><td><button name="del_segundo" id="'+j+'" class="btn btn-danger btn_remove_segundo">X</button></td></tr>');
        $("#tablesegundo").append(input_fila);
        event.preventDefault();
    });
    $(document).on('click','.btn_remove', function () {
        var button_id = $(this).attr("id");
        //$("#row"+button_id+"").remove();
        $("#row"+button_id).remove();
    });
    $(document).on('click','.btn_remove_segundo', function () {
        var button_id = $(this).attr("id");
        //$("#row"+button_id+"").remove();
        $("#rowseg"+button_id).remove();
    });
    $("#sendMenu").click(function( event ) {
        alert("Confirmar que este el menu de hoy");
        $( "#register_menu" ).submit(function( event ) {
            var data_form = $( this ).serializeArray();
            console.log(data_form);
            var data_array = {};
            $.each(data_form,function(){
                data_array[this.name] = this.value;
            });
            console.log(data_array);
            var data_json_form = JSON.stringify(data_array);
            console.log(data_json_form);
            event.preventDefault();
            $.ajax({
                url:'/add_menu',
                type:'POST',
                contentType:'application/json',
                data : data_json_form,
                dataType:'json',
                success: function(response){
                    alert("Menú del día fue registrado exitosamente ");
                    //alert(JSON.stringify(response));
                    //window.location.href="/static/index.html";
                    //$('#allmessages').html("");
                    //$('#action').html(response['statusText']);
                },
                error: function(response){
                    alert("Error: No se pudo registrar el menú");
                    //alert(JSON.stringify(response));
                    //window.location.href="/static/business_register.html";
                    //$('#action').html(response['statusText']);
                }
            });
	    });
    });
});