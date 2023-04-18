let runPy = new Promise(function(success, nosuccess) {

    const { spawn } = require('child_process');
    const pyprog = spawn('python', ['./public/python.py']);
    
    pyprog.stdout.on('data', function(data) {

        success(data);
    });

    pyprog.stderr.on('data', (data) => {

        nosuccess(data);
    });
    
});




const test = (req, res, next) => {

    runPy.then(function(fromRunpy) {
        console.log(fromRunpy.toString());
        res.end(fromRunpy);
    });

};


const location = (req, res) => {
    res.render("index", {title: "Location Test"});
    
};

const about = (req, res) => {
    res.render("about", {title: "about-test"});
};

module.exports = {
    location,
    about,
    test
}