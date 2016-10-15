// Auto-generated. Do not edit!

// (in-package hlpr_speech_msgs.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SpeechServiceRequest {
  constructor() {
    this.get_last = false;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type SpeechServiceRequest
    // Serialize message field [get_last]
    bufferInfo = _serializer.bool(obj.get_last, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type SpeechServiceRequest
    let tmp;
    let len;
    let data = new SpeechServiceRequest();
    // Deserialize message field [get_last]
    tmp = _deserializer.bool(buffer);
    data.get_last = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'hlpr_speech_msgs/SpeechServiceRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '34c3c85c8e7befba1ea4e56d2a4777dd';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    bool get_last
    
    `;
  }

};

class SpeechServiceResponse {
  constructor() {
    this.speech_cmd = '';
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type SpeechServiceResponse
    // Serialize message field [speech_cmd]
    bufferInfo = _serializer.string(obj.speech_cmd, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type SpeechServiceResponse
    let tmp;
    let len;
    let data = new SpeechServiceResponse();
    // Deserialize message field [speech_cmd]
    tmp = _deserializer.string(buffer);
    data.speech_cmd = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'hlpr_speech_msgs/SpeechServiceResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '66b8c3f2415da3d1e6bf60087f6cab82';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    string speech_cmd
    
    
    `;
  }

};

module.exports = {
  Request: SpeechServiceRequest,
  Response: SpeechServiceResponse
};
