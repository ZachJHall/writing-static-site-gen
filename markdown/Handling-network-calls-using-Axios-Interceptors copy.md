---
date: 10-12-21
title: Handling network calls using Axios Interceptors
type: TIL
---

-------
I was recently tasked with setting up a generic way to handle network calls for an application - this led me to Axios Interceptors.

```
// Add a request interceptor
axios.interceptors.request.use(function (config) {
    // Do something before request is sent
    return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });


// Add a response interceptor
axios.interceptors.response.use(function (response) {
    // Any status code that lie within the range of 2xx cause this function to trigger
    // Do something with response data
    return response;
  }, function (error) {
    // Any status codes that falls outside the range of 2xx cause this function to trigger
    // Do something with response error
    return Promise.reject(error);
  });
```
*Code and comments sourced from the [Axios-http](https://axios-http.com/docs/interceptors) site.*

This was extremely helpful and accomplished the heavy lifting of the task.