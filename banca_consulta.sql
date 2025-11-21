USE PROYECTO_BANCA;
GO

-- 1. Ranking 
SELECT 
    RANK() OVER (ORDER BY SUM(monto_miles) DESC) as Ranking,
    banco, 
    FORMAT(SUM(monto_miles), 'N2') as Total_Activos
FROM dbo.banca_consolidado_2018_2024
WHERE anio = 2023 AND indicador = 'TOTAL_ACTIVOS'
GROUP BY banco
ORDER BY Ranking ASC;
go

SELECT 
    RANK() OVER (ORDER BY SUM(monto_miles) DESC) as Ranking_Ganancias,
    banco, 
    FORMAT(SUM(monto_miles), 'N2') as Utilidad_Neta
FROM dbo.banca_consolidado_2018_2024
WHERE anio = 2023 AND indicador = 'UTILIDAD_NETA'
GROUP BY banco
ORDER BY Ranking_Ganancias ASC;
