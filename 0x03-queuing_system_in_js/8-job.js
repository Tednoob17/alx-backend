// Jobs

function createPushNotificationJobs(jobs, queue) {
  if (jobs === undefined || !Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }

  jobs.forEach((job) => {
    const pushNotificationJob = queue.create('push_notification_code_3', job);
    
    pushNotificationJob.save((err) => {
      if (!err) console.log(`Notification job created: ${pushNotificationJob.id}`);
    });

    pushNotificationJob.on('complete', () => {
      console.log(`Notification job ${pushNotificationJob.id} completed`);
    });
    pushNotificationJob.on('failed', (err) => {
      console.log(`Notification job ${pushNotificationJob.id} failed: ${err}`);
    });
    });
  });
}

module.exports = createPushNotificationJobs;
