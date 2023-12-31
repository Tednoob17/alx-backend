// Job Creator

const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

