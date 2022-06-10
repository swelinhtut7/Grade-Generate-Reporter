<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

    <?php
        //initialize values
        if (!isset($_REQUEST['courses'])) { //in case of no value from the form
            $courses = array("CS2101", "CSX2008", "IT1234", "ITX2008");
            $min_a = 85;
            $min_a_minus = 80;
        } else {
            $courses = $_REQUEST['courses'];
            $min_a = $_REQUEST['min_a'];
            $min_a_minus = $_REQUEST['min_a_minus'];
        }   //end if (check array)

      $length = count($courses);
        echo '<br>Length='.$length.'<br>';
        echo '<p>COURSES='. implode(", ", $courses).'</p>';

        //read first element in array
        $current_course = reset($courses);

        //remove first element in array and send it as the hidden data
        //therefore, in the next page, there will be only x-1 elements in the array
        unset($courses[0]);

    ?>

<p>
The grade meeting for <?php echo $current_course; ?>
<br> Codeshare subjects: <?php echo implode(", ",$courses); ?>

<form method="post" action="example.php">
    <?php 
        foreach($courses as $value)
        {
            echo '<input type="hidden" name="courses[]" value="'. $value. '">';
            //echo $value .'<BR>';
        }
    ?>

<input type="hidden" name="current_course" value="<?php echo $current_course; ?>">
A (min): <input type="number" name="min_a" value="<?php echo $min_a; ?>"><br>
A- (min): <input type="number" name="min_a_minus" value="<?php echo $min_a_minus; ?>"> 
 
<br><br>
    <?php
      if ($length > 1) {
    ?>
        <input type="submit" value="Next">
    <?php 
      } else { //display Done button  for the last subject
    ?>
        <input type="submit" value="Done">
    <?php
      } //end if
    ?>

</form>
</p>

</body>
</html>