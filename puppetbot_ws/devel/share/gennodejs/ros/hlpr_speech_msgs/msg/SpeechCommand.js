// Auto-generated. Do not edit!

// (in-package hlpr_speech_msgs.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');
let StampedString = require('./StampedString.js');

//-----------------------------------------------------------

class SpeechCommand {
  constructor() {
    this.stamped_string = new StampedString();
    this.command = '';
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type SpeechCommand
    // Serialize message field [stamped_string]
    bufferInfo = StampedString.serialize(obj.stamped_string, bufferInfo);
    // Serialize message field [command]
    bufferInfo = _serializer.string(obj.command, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type SpeechCommand
    let tmp;
    let len;
    let data = new SpeechCommand();
    // Deserialize message field [stamped_string]
    tmp = StampedString.deserialize(buffer);
    data.stamped_string = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [command]
    tmp = _deserializer.string(buffer);
    data.command = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'hlpr_speech_msgs/SpeechCommand';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8ecdf8b4af928b454a75935476d11010';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # This messages includes the mapping from
    # the detected keyphrase to the command
    
    # Detected keyphrase and its time
    StampedString stamped_string
    # The mapped speech command
    string command
    
    
    
    ================================================================================
    MSG: hlpr_speech_msgs/StampedString
    # Stamped string message to be used in speech recognition
    
    #Time stamp
    time stamp
    #Detected keyphrase
    string keyphrase
    
    `;
  }

};

module.exports = SpeechCommand;
