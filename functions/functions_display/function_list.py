def print_models(unprinted_designs, printed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("printing current design "+ current_design)
        printed_models.append(current_design)

def show_completed_models(printed_models):
    print("\nThe following models have been printed")
    for printed_model in printed_models:
        print(printed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)