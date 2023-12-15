fn day1() {
    const INPUT: &str = include_str!("day1.txt");

    let input_num = INPUT
        .replace("one", "on1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e");

        
    let out = input_num.lines().fold(0, |acc, x| {
        let a = x
            .chars()
            .find(|&c| c > '0' && c <= '9')
            .unwrap()
            .to_digit(10)
            .unwrap() as i32;
        let b = x
            .chars()
            .rfind(|&c| c > '0' && c <= '9')
            .unwrap()
            .to_digit(10)
            .unwrap() as i32;
        acc + a * 10 + b
    });
    println!("{}", out);
    }