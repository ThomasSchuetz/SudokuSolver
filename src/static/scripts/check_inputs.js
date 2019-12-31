// Check that all cells have values, no duplicates, ...

function fill_zeros_if_empty()
{
    for (let row = 0; row < 9; row++) 
    {
        for (let col = 0; col < 9; col++) 
        {
            var current_field = document.getElementsByName("field_"+row+"_"+col)[0];
            if (current_field.value == "") 
            {
                current_field.value = "0";
            }
        }
    }
}

function check_inputs(div_error_message)
{
    var field_error_message = document.getElementsByClassName(div_error_message)[0];
    var solve_button = document.getElementById("btn_solve");

    var error_message = "<b>Before submitting the problem, please fix these errors:</b><br>"

    var messages = "";
    messages += contains_double_entries_horizontal();
    messages += contains_double_entries_vertical();
    messages += contains_double_entries_subfield();

    if (messages != "") 
    {
        field_error_message.style.display = "block";
        field_error_message.innerHTML = error_message + messages;
        solve_button.disabled = true;
    }
    else
    {
        field_error_message.style.display = "none";
        solve_button.disabled = false;
    }
}

function contains_double_entries_horizontal()
{
    var result = "";

    for (let row = 0; row < 9; row++) 
    {
        var entries = [];
        for (let col = 0; col < 9; col++) 
        {
            add_to_field_if_not_empty(entries, document.getElementsByName("field_"+row+"_"+col)[0].value);
        }
        result += add_error_message(enrtries, "Duplicates in row " + (row+1) + "<br>");
    }
    return result;
}


function contains_double_entries_vertical()
{
    var result = "";

    for (let col = 0; col < 9; col++)
    {
        var entries = [];
        for (let row = 0; row < 9; row++)
        {
            add_to_field_if_not_empty(entries, document.getElementsByName("field_"+row+"_"+col)[0].value);
        }
        result += add_error_message(enrtries, "Duplicates in column " + (col+1) + "<br>");
    }
    return result;
}

function contains_double_entries_subfield()
{
    var result = "";

    for (let grid_row = 0; grid_row < 3; grid_row++) 
    {
        for (let grid_col = 0; grid_col < 3; grid_col++)
        {
            var entries = [];
            for (let row = 0; row < 3; row++) 
            {
                for (let col = 0; col < 3; col++) 
                {
                    add_to_field_if_not_empty(entries, document.getElementsByName("field_"+(3*grid_row+row)+"_"+(3*grid_col+col))[0].value);
                }
            }
            result += add_error_message(enrtries, "Duplicates in subfield (" + (grid_row+1) + ", " + (grid_col+1) + ")" + "<br>");
        }
    }
    return result;
}

function has_duplicates(array) {
    return (new Set(array)).size !== array.length;
}

function add_to_field_if_not_empty(array, current_value)
{
    if (current_value != "0" && current_value != "") 
    {
        array.push(current_value);
    }
}

function add_error_message(entries, message)
{
    if (has_duplicates(entries)) 
    {
        return message;
    }
    else
    {
        return "";
    }
}