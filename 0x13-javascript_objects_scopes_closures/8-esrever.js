#!/usr/bin/node
exports.esrever = function (list) {
  const repList = [];
  for (let i = 0; i < list.length; i++) {
    repList.unshift(list[i]);
  }
  return repList;
};
