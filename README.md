# Análisis de los Precios del Taxi en la Ciudad de Nueva York con Spark el día de Año Nuevo

__Abstract__: En este informe se presenta un análisis de la variación de precios en los taxis de la ciudad de Nueva York el primer día del año 2019 usando tecnologías Spark.

Actualmente en el mundo se produce más información que en ninguna otra etapa de la historia, y cada día más. Esto es debido a la dispersión de sistemas inteligentes cada vez más pequeños y eficientes, comenzando por nuestros teléfonos móviles. Muchos de estos datos son producidos por sensores de todo tipo: temperatura, velocidad, tiempo, posicionamiento GPS… A raíz de ello han surgido una serie de portales que aglutinan y comparten gran parte de esta información, principalmente desde organismo públicos, a mayores, en los últimos años se han ido desarrollando una serie de herramientas que permiten procesar estas grandes cantidades de datos de forma escalable y paralela sin que el desarrollador tenga que invertir gran parte de su tiempo en este asunto, en concreto, una de las más extendidas es Spark.

En concreto, en este informe vamos a entender cómo podemos procesar y visualizar la información recogida por los taxis de Nueva York un día que es típicamente muy activo en todo el mundo y que coincide además con las fechas en las que nos encontramos: el primer día del año, en concreto, el 1 de Enero del 2019. La información proporcionada se encuentra en el portal de datos abiertos de la ciudad de Nueva York y con ella vamos a tratar de sacar conclusiones de cómo se comporta la ciudad en cuanto a su movilidad se refiere.

### Resultados

En las gráficas resultantes podemos observar la fluctuación de precios a lo largo del día. Observamos que hay un pico del precio por kilómetro, figura 1, justo a las doce de la noche, cuando, suponemos, habrá un mínimo de conductores y viajeros debido a que la mayoría de los habitantes o turistas de la ciudad se encuentran celebrando el año nuevo, muy típico de esta ciudad.

![](https://github.com/Matesanz/spark/blob/master/images/output.png)

Si observamos la gráfica de la recaudación total, figura 2, a las 00:00 vemos que hay una caída muy significativa de los cobros que en poco minutos vuelve a aumentar fuertemente, consecuencia de la reactivación del tránsito de viajeros justo después de las campanadas.
Poco a poco va descendiendo tanto la actividad total como el ratio precio/distancia hasta alcanzar un valle alrededor de las 6:00 el cual se mantiene durante unas tres o cuatro horas hasta que la ciudad vuelve a revitalizarse y se produce el efecto contrario, pero en este caso ya con subidas más suaves propias de una tarde más normal, estabilizando su precio medio entre los 4.5$ y los 5.0$ por milla recorrida. y ya según va cayendo la noche los precios van reduciéndose de nuevo ante la falta de viajeros y la mejora en la fluidez general del transporte rodado.


![](https://github.com/Matesanz/spark/blob/master/images/output2.png)
