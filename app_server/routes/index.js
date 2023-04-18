const express = require('express');
const router = express.Router();
const homeCtrl = require('../controllers/main.js');
/* GET home page. */
router.get('/', homeCtrl.location);
/* GET about page. */
router.get('/about', homeCtrl.about);
/*GET test python application*/
router.get('/test', homeCtrl.test);

module.exports = router;
