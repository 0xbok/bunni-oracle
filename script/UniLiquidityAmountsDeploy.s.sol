// SPDX-License-Identifier: AGPL-3.0
pragma solidity ^0.8.13;

import "forge-std/Script.sol";
import {UniLiquidityAmounts} from "../src/UniLiquidityAmounts.sol";

contract DeployScript is Script {

    function run() external returns (UniLiquidityAmounts c) {
        uint256 deployerPrivateKey = uint256(vm.envBytes32("PRIVATE_KEY"));

        vm.startBroadcast(deployerPrivateKey);

        c = new UniLiquidityAmounts();

        vm.stopBroadcast();
    }
}
