// Auto-generated. Do not edit!

// (in-package hlpr_speech_msgs.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class StampedString {
  constructor() {
    this.stamp = {secs: 0, nsecs: 0};
    this.keyphrase = '';
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type StampedString
    // Serialize message field [stamp]
    bufferInfo = _serializer.time(obj.stamp, bufferInfo);
    // Serialize message field [keyphrase]
    bufferInfo = _serializer.string(obj.keyphrase, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type StampedString
    let tmp;
    let len;
    let data = new StampedString();
    // Deserialize message field [stamp]
    tmp = _deserializer.time(buffer);
    data.stamp = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [keyphrase]
    tmp = _deserializer.string(buffer);
    data.keyphrase = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'hlpr_speech_msgs/StampedString';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'dab84539140abbb7370c583798723196';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Stamped string message to be used in speech recognition
    
    #Time stamp
    time stamp
    #Detected keyphrase
    string keyphrase
    
    `;
  }

};

module.exports = StampedString;
