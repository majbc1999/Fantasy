%rebase("base.tpl", title="Fantasy Predictor")

<style>
h1 {
    color: blue;
    font-size: 200%;
    text-align: center;
}
h3 {
    color:cornflowerblue;
    font-size: 110%;
    text-align: center;
}
h4 {
    color:midnightblue;
    font-size: 120%;
    text-align: center;
}
table {
    margin-left: auto;
    margin-right: auto;
    width:50%;
}
th {
    text-align: center;
}
td {
  text-align: center;
  width: 25%;
  vertical-align: text-top;
}
label{
    display: inline-block;
    float: center;
    clear: right;
    width: 250px;
    text-align: center;
}
input {
  display: inline-block;
  float: center;
  text-align: center;
}
</style>



<h1> FANTASY PREDICTOR </h1>

<h3> Pozdravljeni v Fantasy Predictorju! </h3>

<table>
<tr>
    <th>
        <h4> PRIJAVA </h4>
    </th>

    <th>
        <h4> REGISTRACIJA (novi uporabniki) </h4>
    </th>
</tr>

<tr>
    <td>
        <form action="/prijava/" method="post">
            <label>uporabniško ime: </label><input name="ime" type="text"><br>
            <br>
            <label>geslo: </label><input name="password" type="password"><br>
            <br>
            <button type="submit">prijava</button>
        </form>
    </td> 

    <td>
        <form action="/prijava/" method="post">
            <label>uporabniško ime: </label><input name="ime" type="text"><br>
            <br>
            <label>geslo: </label><input name="password" type="password"><br>
            <br>
            <label>ponovi geslo: </label><input name="password2" type="password"><br>
            <br>
            <button type="submit">registracija</button>
        </form> <br>
        <i>"Pozor, na novem računu boste imeli 0 točk. Če že imate račun, se raje prijavite." </i>
    </td>
</tr>

</table>
<br><br>
<table>
    <tr><td>
        <form action="/tockovanje/" method="get">
            <button type="submit">pravila točkovanja</button>
        </form>
    </td></tr>
</table>