let funny_number = 69;
var funny_number_new = 69; // i wanted to see if it would throw anything and it did

fn main() {
    // funny_number = 420; okay it's cool that it has language server
    // so there are no assignments to `let`s except maybe `let` is scoped?
    funny_number_new = 420; // but i CAN assign to `var`s from any scope which is interesting
    let funny_number = 67; // why can i do this though?
    // is funny_number scoped??

    if (funny_number == 69) {
        let newgen_number = 67;
    }
    print(funny_number, newgen_number);
}