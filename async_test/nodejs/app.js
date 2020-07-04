const _ = require('lodash');

const AsyncTestClass = async () => {
    let t = [{test: [1]}, {test: [2]}, {test: [3]}, {test: [4]}, {test: [5]}]

    console.time("async example");
    let temp_ex = await asyncTestFunction([1], 'ex')
    console.log('temp ex:', temp_ex)
    console.timeEnd("async example");

    console.time("async Test1");
    let temp1 = await asyncFncType1(t)
    console.log('temp1:', temp1)
    console.timeEnd("async Test1");

    console.time("async Test2");
    let temp2 = await asyncFncType2(t)
    console.log('temp2:', temp2)
    console.timeEnd("async Test2");

    console.time("async Test3");
    let temp3 = await asyncFncType3(t)
    console.log('temp3:', temp3)
    console.timeEnd("async Test3");

    console.time("async Test4");
    let temp4 = await asyncFncType4(t)
    console.log('temp4:', temp4)
    // await Promise.all(asyncTable)
    console.timeEnd("async Test4");
};

const asyncFncType1 = async (table) => {
    _.forEach(table, async (item) => {
        let t = await asyncTestFunction(item['test'], '1')
        item['test'].push(t)
    });
    return table
}

const asyncFncType2 = async (table) => {
    _.map(table, async (item) => {
        let t = await asyncTestFunction(item['test'], '2')
        item['test'].push(t)
    });
    return table
}

const asyncFncType3 = async (table) => {

    let map_t = _.map(table, async (item) => {
        return await asyncTestFunction(item['test'], '3')
    });
    return map_t
}

const asyncFncType4 = async (table) => {

    let map_t = _.map(table, async (item) => {
        return await asyncTestFunction(item['test'], '4')
    });
    return Promise.all(map_t)
}

const sleep = async ms => {
    return new Promise(resolve => {
      setTimeout(resolve, ms);
    });
};

const asyncTestResult = async () => {
    await sleep(5000);
    console.log('asyncTestResult');
    return "Result_TEST"
};

const asyncTestFunction = async (n, v) => {
    await sleep(3000);
    console.log("asyncTestFunction" + v + ": ", n[0]*2);
    return n[0]*2
};




AsyncTestClass()