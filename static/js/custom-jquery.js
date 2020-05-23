function hompage_sudo_solve(){
    grid = $("#grid :input");
    // console.log(grid.value());
    var arr = []
    grid.each(function() {
        element_value = $(this);
        if (element_value.val() == ''){
            arr.push(0);
        }
        else {
            arr.push(Number(element_value.val()));
        }
        
    });
    console.log(arr);
    final_array = splittingalgo(arr);
    // var token = $("[name='csrfmiddlewaretoken']").val();
    // alert(token)
    $.ajax({
        // headers: { "X-CSRFToken": token },
        type: "POST",
        url: 'http://127.0.0.1:8000/',
        data: JSON.stringify(final_array),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(resp) {
            // console.log("_________",resp["board"]);
            solved_array = grouping_algo(resp["board"]);
            grid.each(function(i) {
                element = $(this);
                element.val(solved_array[i]);
                element.attr('disabled','disabled');
            });
            $("#solve-btn").attr('disabled','disabled');
            $("#solve-btn").text('SOLVED');
        },
        error: function (jqXHR, status) {
            // error handler
            console.log(jqXHR);
            //alert('Please Enter Mobile Number');
        }
    });

}

function splittingalgo(arr){
    final_feed = []
    counter = 0;
    for (var i = 1; i < 10; i++) {
        final_feed.push(arr.slice(counter,counter+=9));
      }
    console.log(final_feed);
    return final_feed;
}

function grouping_algo(arr){
    // final_solved = []
    counter = 0;
    new_arr = arr.join();
    var final_solved = new_arr.split(',')    ;
    console.log(final_solved);
    return final_solved;
}