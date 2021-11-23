use std::process::{Command, Stdio};
extern crate colored;
use colored::*;

fn main() {

    let host_output = Command::new("uname")
                     .arg("-n")
                     .stdout(Stdio::piped())
                     .output()
                     .unwrap();

    let mut host_stdout = String::from_utf8(host_output.stdout).unwrap();
    let host_len = host_stdout.len();
    host_stdout.truncate(host_len - 1);

    let user_output = Command::new("users")
                    .stdout(Stdio::piped())
                    .output()
                    .unwrap();

    let mut user_stdout = String::from_utf8(user_output.stdout).unwrap();
    let user_len = user_stdout.len();
    user_stdout.truncate(user_len - 1);

    let os_output = Command::new("uname")
                    .arg("-o")
                    .stdout(Stdio::piped())
                    .output()
                    .unwrap();

    let mut os_stdout = String::from_utf8(os_output.stdout).unwrap();
    let os_len = os_stdout.len();
    os_stdout.truncate(os_len - 1);

    let kernel_output = Command::new("sh")
                    .arg("-c")
                    .arg("uname -rmai | awk '{print $1,$3}'")
                    .stdout(Stdio::piped())
                    .output()
                    .unwrap();

    let mut kernel_stdout = String::from_utf8(kernel_output.stdout).unwrap();
    let kernel_len = kernel_stdout.len();
    kernel_stdout.truncate(kernel_len - 1);

    let uptime_output = Command::new("uptime")
                    .arg("-p")
                    .stdout(Stdio::piped())
                    .output()
                    .unwrap();

    let mut uptime_stdout = String::from_utf8(uptime_output.stdout).unwrap();
    let uptime_len = uptime_stdout.len();
    uptime_stdout.truncate(uptime_len - 1);

    let shell_output = Command::new("sh")
                    .arg("-c")
                    .arg("echo $SHELL")
                    .stdout(Stdio::piped())
                    .output()
                    .unwrap();

    let mut shell_stdout = String::from_utf8(shell_output.stdout).unwrap();
    let shell_len = shell_stdout.len();
    shell_stdout.truncate(shell_len - 1);

    let pacman_output = Command::new("sh")
                    .arg("-c")
                    .arg("pacman -Q | wc -l")
                    .stdout(Stdio::piped())
                    .output()
                    .unwrap();

    let mut pacman_stdout = String::from_utf8(pacman_output.stdout).unwrap();
    let pacman_len = pacman_stdout.len();
    pacman_stdout.truncate(pacman_len - 1);

    let de_output = Command::new("sh")
                    .arg("-c")
                    .arg("echo $DESKTOP_SESSION")
                    .stdout(Stdio::piped())
                    .output()
                    .unwrap();

    let mut de_stdout = String::from_utf8(de_output.stdout).unwrap();
    let de_len = de_stdout.len();
    de_stdout.truncate(de_len - 1);

    let distrib_output = Command::new("sh")
                    .arg("-c")
                    .arg("hostnamectl | grep 'Operating System' | awk '{print $3, $4}'")
                    .stdout(Stdio::piped())
                    .output()
                    .unwrap();

    let mut distrib_stdout = String::from_utf8(distrib_output.stdout).unwrap();
    let distrib_len = distrib_stdout.len();
    distrib_stdout.truncate(distrib_len - 1);

    /*let init_output = Command::new("sh")
                    .arg("-c")
                    .arg("ps -p 1 | grep '1' | awk '{print $4}'")
                    .stdout(Stdio::piped())
                    .output()
                    .unwrap();

    let mut init_stdout = String::from_utf8(init_output.stdout).unwrap();
    let init_len = init_stdout.len();
    init_stdout.truncate(init_len - 1);
    */

    println!("");
    println!("{}                {}@{}", "●".white(), user_stdout, host_stdout);
    println!("{}  ████████████  OS:         {}", "●".red(), distrib_stdout);
    println!("{}  █          █  KERNEL:     {}", "●".blue(), kernel_stdout);
    println!("{}  █          █  UPTIME:     {}", "●".green(), uptime_stdout);
    println!("{}  █          █  PACKAGES:   {}", "●".magenta(), pacman_stdout);
    println!("{}  █▄        ▄█  SHELL:      {}", "●".cyan(), shell_stdout);
    println!("{}   ▀████████▀   DE:         {}", "●".bright_blue(), de_stdout);
    println!("");
}
