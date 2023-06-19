def from_file_to_df(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()

    # Initialize empty lists to store comments and functions
    comments = []
    functions = []


    current_comment = ""
    current_function = ""
    for line in lines:
        line = line.strip()
        if line.startswith("#'"):
            current_comment += line[2:] + " "
            if current_function:
                current_function = current_function + ' \n\n###\n\n'
                functions.append(current_function)
                current_function = ""
        else:
            current_function += line + " "
            if current_comment:
                current_comment = current_comment
                comments.append(current_comment.strip())
                current_comment = ""


    # If there are remaining comments or functions after the last function
    if current_comment:
        comments.append(current_comment.strip())
    if current_function:
        functions.append(current_function.strip())
    df = pd.DataFrame({"Comments": comments, "Functions": functions})
    df.rename(columns={'Comments':'prompt', 'Functions':'completion'}, inplace=True)
    return df