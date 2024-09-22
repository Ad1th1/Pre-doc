import subprocess

def run_c_program():
    
    compile_command = ["gcc", "1.c", "-o", "lol", "-lrt", "-lm"]
    subprocess.run(compile_command, check=True)

    with open("output.txt", "w") as outfile:
        for i in range(300):
            result = subprocess.run(["./lol"], capture_output=True, text=True)

            output = result.stdout.strip() 
            if "Access time" in output:
                cycles = output.split()[2]  
                outfile.write(f"{cycles}\n") 


if __name__ == "__main__":
    run_c_program()
    print("Done! Lol")
