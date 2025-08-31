import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [signUpUser(firstName, lastName), uploadPhoto(fileName)];

  return Promise.allSettled(promises).then((results) =>
    results.map((res) => {
      if (res.status === 'fulfilled') {
        return { status: res.status, value: res.value };
      } else {
        return { status: res.status, value: res.reason.toString() };
      }
    })
  );
}