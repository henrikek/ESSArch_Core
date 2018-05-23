import angular from 'angular';

import loginCtrl from './controllers/LoginCtrl';

export default angular
    .module('essarch.authentication', [])
    .controller('LoginCtrl', loginCtrl).name;
