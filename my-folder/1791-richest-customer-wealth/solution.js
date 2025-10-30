/**
 * @param {number[][]} accounts
 * @return {number}
 */
 const maximumWealth = (arr) => {
  const newArr = arr.map((currentValue) => currentValue.reduce((acc,curr) => acc+ curr));
  return Math.max(...newArr);
};
