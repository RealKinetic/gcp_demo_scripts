#!/bin/bash

if [ -z "$1" ]
then
  echo "You must pass in a topic name to create and subscribe to."
else
  echo Creating pubsub topic: $1
  gcloud pubsub topics create $1
  echo Finished creating pubsub topic: $1

  if [ -z "$2" ]
  then
    echo "No subscription name given. Subscription not created."
  else
    echo Creating pubsub subscription: $2 to topic: $1
    gcloud pubsub subscriptions create $2 --topic $1
    echo Fiished creating pubsub subscription: $2 to topic: $1
  fi
fi
