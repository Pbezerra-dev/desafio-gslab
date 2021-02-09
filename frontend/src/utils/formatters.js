export const formatCurrency = n =>
  /**
   * Receive format xxxxxx.xx
   * Convert format to R$ xxx.xxx,xx
   * */
  parseFloat(n.replace(',', '.')).toLocaleString('pt-br', {
    style: 'currency',
    currency: 'BRL'
  })
