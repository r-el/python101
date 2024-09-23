const fs = require('fs');
const path = require('path');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const getDirectories = source =>
    fs.readdirSync(source, { withFileTypes: true })
        .filter(dirent => dirent.isDirectory())
        .map(dirent => dirent.name);

const mainDirectory = '/home/ariel/Documents/python/python101'; // Change this to your main directory path
const directories = getDirectories(mainDirectory).slice(0, 99);

console.log('Please choose a directory by entering a number between 0 and 99:');
directories.forEach((dir, index) => {
    console.log(`${index}: ${dir}`);
});

rl.question('Enter the number corresponding to the directory: ', (answer) => {
    const dirIndex = parseInt(answer, 10);
    if (isNaN(dirIndex) || dirIndex < 0 || dirIndex >= directories.length) {
        console.log('Invalid number. Please restart the script and enter a valid number.');
        rl.close();
        return;
    }

    const directoryPath = path.join(mainDirectory, directories[dirIndex]);
    const outputFileName = `${path.basename(directoryPath)}.py`;

    rl.question('Do you want to merge files from subdirectories as well? (yes/no): ', (mergeSubDirsAnswer) => {
        const mergeSubDirs = mergeSubDirsAnswer.toLowerCase() === 'yes';

        const getAllFiles = (dir, allFiles = []) => {
            const files = fs.readdirSync(dir, { withFileTypes: true });
            files.forEach(file => {
                const filePath = path.join(dir, file.name);
                if (file.isDirectory() && mergeSubDirs) {
                    getAllFiles(filePath, allFiles);
                } else if (file.isFile() && path.extname(file.name) === '.py') {
                    allFiles.push(filePath);
                }
            });
            return allFiles;
        };

        const files = getAllFiles(directoryPath);

        let mergedContent = '';

        files.forEach(file => {
            const fileContent = fs.readFileSync(file, 'utf8');
            mergedContent += `# ${path.relative(directoryPath, file)}\n${fileContent}\n\n\n`;
        });

        fs.writeFileSync(path.join(directoryPath, outputFileName), mergedContent);
        console.log(`Successfully merged Python files into ${outputFileName}`);
        rl.close();
    });
});