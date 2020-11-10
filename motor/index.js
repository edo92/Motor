const { PythonShell } = require('python-shell');

let options = {
    mode: 'text',
    pythonOptions: ['-u'], // get print results in real-time
    args: ['moveF', 'row1', '5', '100']
};

PythonShell.run('main.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log('results: %j', results);
});