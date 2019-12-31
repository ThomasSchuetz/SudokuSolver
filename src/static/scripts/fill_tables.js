// Assume empty puzzle and fill this with values (e.g. result or initial puzzle)

function initialize_puzzle(prefix="field_")
{
    for (let row = 0; row < 9; row++) 
    {
        for (let col = 0; col < 9; col++) 
        {
            var current_field = document.getElementsByName(prefix + row + "_" + col)[0];
            update_field(current_field, "0");
        }
    }   
}

function adjust_style(selected_input)
{
    if (selected_input.value === '' || selected_input.value == "0") 
    {
        selected_input.style.color = "white";
    }
    else 
    {
        selected_input.style.color = "black";
    }
}

function fill_puzzle(inputs, prefix="field_")
{
    for (let row = 0; row < inputs.length; row++) 
    {
        for (let col = 0; col < inputs[row].length; col++) 
        {
            var current_field = document.getElementsByName(prefix + row + "_" + col)[0];
            update_field(current_field, inputs[row][col]);
        }
    }
}

function update_field(field, value)
{
    field.value = value;
    adjust_style(field);
}

function update_background_colors(inputs, prefix="field_")
{
    for (let row = 0; row < 9; row++) 
    {
        for (let col = 0; col < 9; col++) 
        {
            var current_field = document.getElementsByName(prefix + row + "_" + col)[0];

            if (current_field.value == inputs[row][col]) {
                current_field.style.backgroundColor = "grey";
            }
        }
    }   
}