$(document).ready(function () {
	$("#n1").val("");
	$("#m1").val("");
	op = "";
	$("#muestra").val("");

	$("#n1").on("click",
		function () { $("#n1").val(""); });
	$("#c").on("click",
		function () {
			$("#n1").val("");
			op = "";
			$("#muestra").val("");
		});
	$("#tom").on("click",
		function () {
			var m1 = $("#n1");
			$("#m1").val(m1.val());
		});

	$("#fromM").on("click",
		function () {
			var num = $("#m1");
			$("#n1").val(num.val());
		});

	$(".arras").draggable({ revert: true });

	$(".sueltaN").droppable({
		drop: function (event, ui) {
			var num = $("#n1");
			$("#m1").val(num.val());
		}
	});

	$(".sueltaM").droppable({
		drop: function (event, ui) {
			var num = $("#m1");
			$("#n1").val(num.val());
		}
	});

	$(".val").on("click",
		function (e) {
			e.preventDefault();
			var a = $(this).attr("href");
			$("#n1").val($("#n1").val() + a);
		});

	$("#cuadrado").on("click",
		function () {
			var num = $("#n1");
			$("#n1").val(num.val() * num.val());
		});
	$("#inverso").on("click",
		function () {
			var num = $("#n1");
			$("#n1").val(1 / num.val());
		});
	$("#raiz").on("click",
		function () {
			var num = $("#n1");
			$("#n1").val(Math.sqrt(num.val()));
		});
	$("#parte_entera").on("click",
		function () {
			var num = $("#n1");
			if (num.val() >= 0) {
				$("#n1").val(Math.floor(num.val()));

			} else {
				$("#n1").val(-Math.ceil(num.val()));
			}
		});
	$("#n").on("click",
		function () {
			var num = $("#n1");
			$("#n1").val(Math.pow(2, +num.val()));
		});

	$("#fact").on("click",
		function () {
			var num = $("#n1"); var total = 1;
			for (var n = 1; n <= num.val(); n++) { total = total * n; }
			$("#n1").val(total);
		});


	$("#suma").on("click",
		function () {
			num = $("#n1");
			acc = num.val();
			op = op + acc + "+";
			$("#muestra").val(op);
			$("#n1").val("");
		});
	$("#resta").on("click",
		function () {
			num = $("#n1");
			acc = num.val();
			op = op + acc + "-";
			$("#muestra").val(op);
			$("#n1").val("");
		});
	$("#por").on("click",
		function () {
			num = $("#n1");
			acc = num.val();
			op = op + acc + "*";
			$("#muestra").val(op);
			$("#n1").val("");
		});
	$("#entre").on("click",
		function () {
			num = $("#n1");
			acc = num.val();
			op = op + acc + "/";
			$("#muestra").val(op);
			$("#n1").val("");
		});

	$("#parentesis").on("click",
		function () {
			num = $("#n1");
			acc = num.val();
			if (op.lastIndexOf("(") <= op.lastIndexOf(")")) {
				op = op + acc + "(";
			} else {
				op = op + acc + ")";
			}

			$("#muestra").val(op);
			$("#n1").val("");
		});

	$("#sumatorio").on("click",
		function () {
			var num = $("#n1"); listado = num.val().split(",");
			for (var n = 0, total = 0; n < listado.length; n++) { total = +total + (+listado[n]); }
			$("#n1").val(total);
		});
	$("#producto").on("click",
		function () {
			var num = $("#n1"); listado = num.val().split(",");
			for (var n = 0, total = 1; n < listado.length; n++) { total = +total * +listado[n]; }
			$("#n1").val(total);
		});

	$("#igual").on("click",
		function () {
			var num = $("#n1");
			acc = num.val();
			op += acc;
			$("#muestra").val(op);
			$("#n1").val(eval(op));
			op = "";

			var num = $("#n1");
			if (op === "+") {
				$("#n1").val(+acc + (+num.val()));
			}
			if (op === "-") {
				$("#n1").val(+acc - (+num.val()));
			}
			if (op === "*") {
				$("#n1").val(+acc * (+num.val()));
			}
			if (op === "/") {
				$("#n1").val(+acc / (+num.val()));
			}
			if (op === "e") {
				$("#n1").val(Math.pow(+acc, +num.val()));
			}
		});
});

function sorpresa() {
	alert("Ha ganado un IPhone, dígite su contraseña de Google para reclamarlo");
};

function hexadecimal() {
	var obj1 = 0, resul1 = 0;
	
    obj1 = document.getElementById("n1").value;
	obj1 = parseInt(obj1);
    resul1 = obj1.toString(16);
	console.log(resul1);
	document.getElementById("n1").value = resul1;
};

function fibonacci() {
	var obj = document.getElementById("n1").value;
    var a=1, b=1;

    for (let i = 2; i < obj; i++) {
        c=a+b;
        a=b;
        b=c;
	}

    document.getElementById("n1").value = c;
};

function sumatoria() {
	var obj = document.getElementById("n1").value;
	var sumatoria = 0 ;

	for (let i = 0; i < obj; i++) {
		sumatoria += i;
	}

	document.getElementById("n1").value = sumatoria;
};