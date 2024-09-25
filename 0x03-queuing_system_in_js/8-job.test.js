import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
        {
            phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
        },
        {
            phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
        }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(jobs.length);

    queue.testMode.jobs.forEach((job, index) => {
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.deep.equal(jobs[index]);
    });
  });
});