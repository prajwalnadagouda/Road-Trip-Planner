<?php
    function dispRecommendationBox($sql, $conn, $username = null) {

        $result = $conn->query($sql);

        if ($result && $result->num_rows > 0) {

        $curl = curl_init('http://localhost:9090/recommendations');
        $options = array(
            CURLOPT_RETURNTRANSFER => true,   // return web page
            CURLOPT_HEADER         => false,  // don't return headers
            CURLOPT_FOLLOWLOCATION => true,   // follow redirects
            CURLOPT_MAXREDIRS      => 10,     // stop after 10 redirects
            CURLOPT_ENCODING       => "",     // handle compressed
            CURLOPT_USERAGENT      => "test", // name of client
            CURLOPT_AUTOREFERER    => true,   // set referrer on redirect
            CURLOPT_CONNECTTIMEOUT => 120,    // time-out on connect
            CURLOPT_TIMEOUT        => 120,    // time-out on response
        );
        curl_setopt_array($curl, $options);

        $response  = curl_exec($curl);
        curl_close($curl);
        $res_json = json_decode($response, true);
        #print_r($res_json["parks"]);

    ?>
        <div class="panel panel-default">
            <?php while ($tpref = $result->fetch_assoc()) { ?>
            <h4 style="display:center;">
                <?php switch($tpref['preference']) {
                    case "events": echo "Events";
                    break;
                    case "parks": echo "Parks";
                    break;
                    case "amusementparks": echo "Amusement Parks";
                    break;
                    case "museums": echo "Museums";
                    break;
                    case "restaurants": echo "Restaurants";
                    break;
                }
                ?>
            </h4>
            <div class="panel-body" style="margin-top:20px;margin-bottom:20px;">
                <?php foreach($res_json[$tpref['preference']] as $i => $i_value) { ?>
                <div class="friend-box" style="margin-top:5px;margin-bottom:5px;">
                        <div class="" >
                            <?php switch($tpref['preference']) {
                                case "events": switch($i_value['event_type']){
                                    case "concerts": echo "Concert";
                                    break;
                                    case "theater": echo "Theatre";
                                    break;
                                    case "sports": echo "Sport";
                                }
                                echo " by " . $i_value['event_performer'];
                                break;
                                default: echo $i_value['name'];
                                /* case "parks": echo $i_value['name'];
                                break;
                                case "amusementparks": echo $i_value['name'];
                                break;
                                case "museums": echo $i_value['name'];
                                break;
                                case "restaurants": echo $i_value['name'];
                                break; */
                            }
                            ?>
                        </div>
                </div>
                <?php } ?>
            </div>
            <?php } ?>
        </div>
        <?php } else { ?>
            <p class="text-center">Nothing to display yet!</p>
        <?php }
    } ?>
