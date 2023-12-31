// Job Processor

const kue = require('kue');
const queue = kue.createQueue();

const blacklistedPhoneNumbers = [
  '4153518780',
  '4153518781',
];


queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
  done();
});
