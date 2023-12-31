// Job Creator

const kue = require('kue');
const queue = kue.createQueue();

const jobs = [
  pushNotificationJob.on('complete', () => {
    console.log(`Notification job ${pushNotificationJob.id} completed`);
  });

  pushNotificationJob.on('failed', (errorMessage) => {
    console.log(`Notification job ${pushNotificationJob.id} failed: ${errorMessage}`);
  });

  pushNotificationJob.on('progress', (progress) => {
    console.log(`Notification job ${pushNotificationJob.id} ${progress}% complete`);
  });
});
