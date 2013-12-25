<!DOCTYPE html>
<html>
    <head>
        <title>Hacker News Recorder</title>
        <link rel="stylesheet" type="text/css" href="./contents/default.css">
    </head>
    <body>
    <div id="box">
        <div id="box_title">
            <h1 class="logo">Hacker News Recorder</h1> 
        </div>
        <ol>
            % for x in data:
                <li>
                    <div class="title">
                        <a href={{x["link"]}}>{{x["title"]}}</a>
                    </div>
                    <div class="subtext">
                        {{x["points"]}} pt. | 
                        <a href={{x["comments_link"]}}>{{x["num_comments"]}}</a> comments. | 
                        <a href={{x["submitter_profile"]}}>{{x["submitter"]}}</a> |
                        {{x["domain"]}} |
                        {{x["published_time"]}}
                    </div>
                </li>
            % end
        </ol>
        <div id="box_bottom">
            <a href="#" id="bottom_text">Top</a>
        </div>
    <div>
    </body>
</html>



