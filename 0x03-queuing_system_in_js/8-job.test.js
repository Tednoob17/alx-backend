// Job Tests

import kue from 'kue';
import createPushNotificationsJobs from './8-job';
import { describe, it } from 'mocha';
import { expect } from 'chai';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
    beforeEach(() => {
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
    });

    after(() => {
        queue.testMode.exit();
    });

    it('display a error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('job', queue)).to.throw('Jobs is not an array');
    });

    it('create two new jobs to the queue', () => {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 4562 to verify your account'
            }
        ];

