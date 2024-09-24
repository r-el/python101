const fs = require('fs');
const path = require('path');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter the number of exercises: ', (numOfExercises) => {
    rl.question('Enter the first exercise number: ', (firstExerciseNum) => {
        rl.question('Enter the directory path (leave empty for default "src"): ', (dirPath) => {
            const targetPath = dirPath.trim() || 'src';
            generatePythonFiles(parseInt(numOfExercises), parseInt(firstExerciseNum), targetPath);
            rl.close();
        });
    });
});

function generatePythonFiles(numOfExercises, firstExerciseNum, dirPath) {
    const fullPath = path.join(dirPath);
    fs.mkdirSync(fullPath, { recursive: true });
    for (let i = firstExerciseNum; i < firstExerciseNum + numOfExercises; i++) {
        const fileName = `${i}.py`;
        const pythonCode = `
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
        `;
        fs.writeFileSync(path.join(fullPath, fileName), pythonCode);
    }
    console.log(`Successfully created ${numOfExercises} Python files in ${fullPath}.`);
}
